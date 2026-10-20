package com.strikevector.controller;

import android.app.Activity;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebView;

// Thin shell: the UI is race.html from assets; tilt comes from SensorManager through window.nativeTilt(gamma, beta)
// so no browser sensor-permission gate (Chrome, Brave shields, ...) is involved.
public class MainActivity extends Activity implements SensorEventListener {
    private WebView web;
    private SensorManager sensors;
    private final float[] rot = new float[9], orient = new float[3];
    private long lastPush = 0;

    @Override protected void onCreate(Bundle saved) {
        super.onCreate(saved);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        web = new WebView(this);
        web.getSettings().setJavaScriptEnabled(true);
        web.getSettings().setDomStorageEnabled(true);   // localStorage keeps the server address
        web.setBackgroundColor(0xFF15171A);
        setContentView(web);
        web.loadUrl("file:///android_asset/race.html");
        sensors = (SensorManager) getSystemService(SENSOR_SERVICE);
    }

    @Override protected void onResume() {
        super.onResume();
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION);
        Sensor s = sensors.getDefaultSensor(Sensor.TYPE_GAME_ROTATION_VECTOR);
        if (s == null) s = sensors.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR);
        if (s != null) sensors.registerListener(this, s, SensorManager.SENSOR_DELAY_GAME);
    }

    @Override protected void onPause() { super.onPause(); sensors.unregisterListener(this); }

    @Override public void onSensorChanged(SensorEvent e) {
        long now = e.timestamp / 1_000_000;
        if (now - lastPush < 25) return;              // ~40 Hz is plenty for a 30 Hz send loop
        lastPush = now;
        SensorManager.getRotationMatrixFromVector(rot, e.values);
        SensorManager.getOrientation(rot, orient);    // [azimuth, pitch, roll] in radians
        float beta = (float) Math.toDegrees(-orient[1]);   // front/back tilt, like DeviceOrientation beta
        float gamma = (float) Math.toDegrees(orient[2]);   // left/right roll, like DeviceOrientation gamma
        web.evaluateJavascript("window.nativeTilt&&nativeTilt(" + gamma + "," + beta + ")", null);
    }

    @Override public void onAccuracyChanged(Sensor sensor, int accuracy) {}
}
