﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

/// <summary>
/// Stream performance data via UDP connection
/// </summary>
public class SP_PerfLiveStreamer : MonoBehaviour {
	Socket sending_socket = new Socket(
		AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
	IPAddress send_to_address;
	IPEndPoint sending_end_point;
	private const int port_number = 11000;

	void Awake() {
		// set IP address accordingly
		switch (PublicSettings.UDP_DEBUG_MODE) {
			case PublicSettings.UDP_LOCAL_MODE:
				this.send_to_address = IPAddress.Parse("127.0.0.1");
				break;
			case PublicSettings.UDP_RELEASE_MODE:
				this.send_to_address = IPAddress.Parse("169.254.143.183");
				break;
			case PublicSettings.UDP_ETHERNET_MODE:
				this.send_to_address = IPAddress.Parse("169.254.143.183");
				break;
		}
		// configure target endPoint (IP, port)
		this.sending_end_point = new IPEndPoint(send_to_address, port_number);
	}

	/// <summary>
    /// Stream performance data over UDP for live monitoring
    /// </summary>
	/// <param name="p">An instance of <see cref="Performance"/> class</param>
	public void StreamSendData(Performance p) {
		// prepare buffer
		byte[] send_buffer = Encoding.ASCII.GetBytes(JsonUtility.ToJson(p));
		try {
			sending_socket.SendTo(send_buffer, sending_end_point);
		} catch (Exception e) {
			Debug.Log(e.Message);
		}
	}
}
