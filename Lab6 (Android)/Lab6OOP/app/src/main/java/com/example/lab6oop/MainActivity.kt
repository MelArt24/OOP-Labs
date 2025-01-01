package com.example.lab6oop

import android.content.Intent
import android.content.Intent.FLAG_ACTIVITY_SINGLE_TOP
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    private lateinit var nPointEditText: EditText
    private lateinit var xMinEditText: EditText
    private lateinit var xMaxEditText: EditText
    private lateinit var yMinEditText: EditText
    private lateinit var yMaxEditText: EditText
    private lateinit var submitButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        nPointEditText = findViewById(R.id.edit_text_nPoint)
        xMinEditText = findViewById(R.id.edit_text_xMin)
        xMaxEditText = findViewById(R.id.edit_text_xMax)
        yMinEditText = findViewById(R.id.edit_text_yMin)
        yMaxEditText = findViewById(R.id.edit_text_yMax)
        submitButton = findViewById(R.id.submit_button)

        submitButton.setOnClickListener {
            val nPoint = nPointEditText.text.toString().toIntOrNull() ?: 10
            val xMin = xMinEditText.text.toString().toIntOrNull() ?: 0
            val xMax = xMaxEditText.text.toString().toIntOrNull() ?: 100
            val yMin = yMinEditText.text.toString().toIntOrNull() ?: 0
            val yMax = yMaxEditText.text.toString().toIntOrNull() ?: 100

            if (xMax <= xMin || yMax <= yMin) {
                Toast.makeText(this, "Incorrect ranges: xMax must " +
                        "be > xMin, yMax must be > yMin", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            val obj2Intent: Intent? = packageManager.getLaunchIntentForPackage("com.example.object2")
            obj2Intent?.let {

                Log.d(
                    "MainActivity",
                    "Running object2 with parameters: nPoint=$nPoint, xMin=$xMin, xMax=$xMax, yMin=$yMin, yMax=$yMax"
                )

                it.addFlags(FLAG_ACTIVITY_SINGLE_TOP) // does not create a new activity if it is already running
                it.putExtra("nPoint", nPoint)
                it.putExtra("xMin", xMin)
                it.putExtra("xMax", xMax)
                it.putExtra("yMin", yMin)
                it.putExtra("yMax", yMax)
                startActivity(it) // launches the application object2
            } ?: run { // Handling the situation if object2 is unavailable
                Toast.makeText(this, "The object2 application is not installed or unavailable", Toast.LENGTH_SHORT).show()
                Log.e("MainActivity", "com.example.object2 not found")
            }
        }

    }
}