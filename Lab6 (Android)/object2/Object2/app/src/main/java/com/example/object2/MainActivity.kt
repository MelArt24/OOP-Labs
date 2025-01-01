package com.example.object2

import android.annotation.SuppressLint
import android.content.ClipData
import android.content.ClipboardManager // ClipboardManager: for copying text to the clipboard
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        generatePoints()
        val obj3Intent: Intent? = packageManager.getLaunchIntentForPackage("com.example.object3")
        if (obj3Intent != null) {
            obj3Intent.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP)
            startActivity(obj3Intent)
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        setIntent(intent)
        generatePoints()
        val obj3Intent: Intent? = packageManager.getLaunchIntentForPackage("com.example.object3")
        obj3Intent!!.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP)
        startActivity(obj3Intent)
    }

    @SuppressLint("SetTextI18n")
    private fun generatePoints() {

        val extras = intent.extras // receives additional data passed via intent
        if (extras == null) {
            val textView: TextView = findViewById(R.id.textView)
            textView.text = "No data received."
            return
        }

        val nPoint = intent.extras!!.getInt("nPoint")
        val xMin = intent.extras!!.getInt("xMin")
        val xMax = intent.extras!!.getInt("xMax")
        val yMin = intent.extras!!.getInt("yMin")
        val yMax = intent.extras!!.getInt("yMax")

        val textView: TextView = findViewById(R.id.textView)

        val points = mutableListOf<Pair<Int, Int>>()
        for (i in 1..nPoint) {
            val randX = Random.nextInt(xMin, xMax)
            val randY = Random.nextInt(yMin, yMax)
            points.add(Pair(randX, randY))
        }

        points.sortBy { point -> point.first }

        var string = "X\t\t\tY\n"

        for (i in points.indices) {
            string += points[i].first.toString() + "\t\t\t" + points[i].second.toString() + "\n"
        }
        textView.text = string.trim('\n')

        // ClipboardManager: copies text to the clipboard.
        val clipboard = getSystemService(CLIPBOARD_SERVICE) as ClipboardManager
        val clip = ClipData.newPlainText("coords", textView.text)
        clipboard.setPrimaryClip(clip)
    }
}