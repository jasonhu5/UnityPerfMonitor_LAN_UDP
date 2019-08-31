# Unity Performance Monitor over LAN with UDP

#### A demo video is available at [this link](https://youtu.be/WgAZL7bsXec).
In this project, a Unity program performs trials with a player, and the tool helps getting the live performance results and plot it for trends analysis. The incentive is that some distributed Unity program builds have no option for console or live data monitor, and the live data can sometimes be important and should be checked by a non-player. A typical setup with such need is a clinical game. Underlying technology is simple, Unity serves as a UDP sender (host) and a Python program receives, processes and presents the data (client).


* ### [Installation](#installation-1)
* ### [Preparation for use](#preparation-for-use-1)
* ### [How to use](#how-to-use-1)


---

### Installation
* clone or download this repository
* Place ___[Performance.cs](https://github.com/jasonhu5/UnityPerfMonitor_LAN_UDP/blob/master/Performance.cs)___ and ___[PerfLiveStreamer.cs](https://github.com/jasonhu5/UnityPerfMonitor_LAN_UDP/blob/master/PerfLiveStreamer.cs)___ in Unity Scripts location.

### Preparation for use
##### Inject performance (metric) class in Unity script
* The Performance class describes a definition for performance metrics. The components of a performance record are:
    * if the response given by game player is as expected
    * how long the player spent to give such a response
    * what current difficulty level is

* Simply create an instance of Performance to be streamed as shown below

```csharp
// Constructor for Performance class.
// Performance(bool isCorrect, float timeUsed, float difficulty)

// Create an instance of Performance class.
private Performance perf = new Performance(
    response == true_answer,
    elapsed_time,
    current_difficulty_level
)
```

##### Inject the Unity host streamer in Unity script AND scene
* Put an empty GameObject in the scene, and attach the PerfLiveStreamer script to that object.
* Add code for streamer in a high level logic control script, where the game is iterative within that script (somewhat like a ___main___ program). 
```csharp
/// <value>A UDP streamer that sends performance data.</value>
/// <remark> Deactivate game object in Unity to not send such data.</remark>
public PerfLiveStreamer streamer;
```
* Send the performance data if the gameObject is active
```csharp
// send performance data for live monitoring
if (streamer.transform.gameObject.activeSelf) {
    streamer.StreamSendData(perf);
}
```

##### Changing IP address accordingly in BOTH Unity script and Python script
* In Unity, change the `send_to_address` in PerfLiveStreamer to the IP address of host machine in LAN.
* In the Python file, change `UDP_IP` for ethernet mode. A shortcut for localhost mode is created for faster testing, in practical use, i.e. host-client LAN connection, it's always in "ethernet" mode for the Python script.

### How to use
* Start the Python client program from terminal
    * local mode: `python UDP_stats.py 0`
    * or LAN/ethernet mode: `python UDP_stats.py 0`
* Run Unity program, with streamer game object enabled.

### Presentations
* In terminal, the python program outputs performance metrics as processed text.
* A plot figure pops up, with each new performance data received, a new point appears on the figure.