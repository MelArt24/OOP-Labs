package com.example.object3

import android.content.ClipboardManager
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.github.mikephil.charting.charts.LineChart
import com.github.mikephil.charting.data.LineData
import com.github.mikephil.charting.data.LineDataSet
import com.github.mikephil.charting.data.Entry

class MainActivity : AppCompatActivity() {

    private lateinit var lineChart: LineChart // widget for displaying a graph
    private lateinit var copiedData: String // a string with dots, retrieved from the clipboard
    // minimum and maximum X and Y values for graph scaling
    private lateinit var minAndMaxX: Pair<Float, Float>
    private lateinit var minAndMaxY: Pair<Float, Float>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onWindowFocusChanged(hasFocus: Boolean) {
        super.onWindowFocusChanged(hasFocus)

        if (hasFocus) {
            val clipboard = getSystemService(CLIPBOARD_SERVICE) as ClipboardManager
            val copiedPointsString = clipboard.primaryClip?.getItemAt(0)?.text?.toString()
            copiedData = copiedPointsString.toString()

            lineChart = findViewById(R.id.lineChart)
            lineChart.clear()

            // Converts a line of points into data for a graph
            val dataSet = getSeriesFromString(copiedData)

            val lineData = LineData(dataSet)

            lineChart.data = lineData
            lineChart.animateXY(1000, 1000) // Animation

            lineChart.setTouchEnabled(true)  // Allow interaction
            lineChart.isDragEnabled = true  // Allow dragging
            lineChart.setScaleEnabled(true) // Allow scaling
            lineChart.setPinchZoom(true)  // Enable scaling for both axes

            // Setting minimums and maximums for axes
            lineChart.axisLeft.axisMinimum = 0f
            lineChart.axisLeft.axisMaximum = minAndMaxY.second + 1f
            lineChart.axisRight.isEnabled = false
            lineChart.xAxis.axisMinimum = 0f
            lineChart.xAxis.axisMaximum = minAndMaxX.second + 1f

            lineChart.xAxis.position = com.github.mikephil.charting.components.XAxis.XAxisPosition.BOTTOM

            lineChart.invalidate() // Graph update
        }
    }

    // Converts a line of points into data for a graph
    private fun getSeriesFromString(str: String): LineDataSet {
        val pointsStrArray = str.trimEnd('\n').split("\n").toMutableList().also { it.removeAt(0) }
        val pointsList = mutableListOf<Entry>()
        var minX: Float = pointsStrArray[0].split("\t\t\t")[0].toFloat()
        var maxX: Float = pointsStrArray[pointsStrArray.size - 1].split("\t\t\t")[0].toFloat()
        var minY: Float = pointsStrArray[0].split("\t\t\t")[1].toFloat()
        var maxY: Float = minY

        for (i in pointsStrArray.indices) {
            val x = pointsStrArray[i].split("\t\t\t")[0].toFloat()
            val y = pointsStrArray[i].split("\t\t\t")[1].toFloat()
            if (i == 0) {
                minX = x
            } else if (i == pointsStrArray.size - 1) {
                maxX = x
            }

            if (y < minY) {
                minY = y
            }
            if (y > maxY) {
                maxY = y
            }
            pointsList.add(Entry(x, y))
        }
        minAndMaxX = Pair(minX, maxX)
        minAndMaxY = Pair(minY, maxY)

        return LineDataSet(pointsList, "Data").apply {
            setDrawValues(false) // Do not show values near points
            setDrawCircles(true) // Draw circles on points
            circleRadius = 5f
            color = resources.getColor(R.color.red) // Line color
        }
    }
}
