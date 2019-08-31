using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// A preformance record for a trial
/// </summary>
public class Performance
{
    public bool isCorrect;
    public float timeUsed;
    public float difficulty;

    /// <summary>
    /// Initializes a new instance of the <see cref="Performance"/> class.
    /// </summary>
    /// <param name="isCorrect">Trial response is correct</param>
    /// <param name="timeUsed">Time for getting a response</param>
    /// <param name="difficulty">Trial difficulty level</param>
    public Performance(
        bool isCorrect,
        float timeUsed,
        float difficulty
    ) {
        this.isCorrect = isCorrect;
        this.timeUsed = timeUsed;
        this.difficulty = difficulty;
    }
}
