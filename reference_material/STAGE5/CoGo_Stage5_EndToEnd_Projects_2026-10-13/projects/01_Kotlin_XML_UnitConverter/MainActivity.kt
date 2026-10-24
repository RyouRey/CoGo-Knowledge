package com.example.unitconverter

import android.app.Activity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.util.Locale

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val input = findViewById<EditText>(R.id.inputCentimeters)
        val convertButton = findViewById<Button>(R.id.buttonConvert)
        val result = findViewById<TextView>(R.id.textResult)

        convertButton.setOnClickListener {
            val raw = input.text.toString().trim()
            val centimeters = raw.toDoubleOrNull()

            if (centimeters == null || !centimeters.isFinite() || centimeters < 0.0) {
                result.text = "Enter a valid number (0 or greater)."
            } else {
                val inches = centimeters / 2.54
                result.text = String.format(
                    Locale.US,
                    "%.2f cm = %.2f in",
                    centimeters,
                    inches
                )
            }
        }
    }
}
