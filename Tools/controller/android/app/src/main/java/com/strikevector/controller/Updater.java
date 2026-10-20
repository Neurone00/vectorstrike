package com.strikevector.controller;

import android.app.Activity;
import android.app.DownloadManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.Uri;
import android.os.Build;
import android.os.Environment;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

// Self-update from GitHub releases: newest "controller-vX.Y" tag with an .apk asset. Android cannot
// install silently outside a store, so the system installer still asks the user to confirm.
// Each release must raise versionCode (see release.sh), or the installer refuses the update.
public final class Updater {
    static final String LATEST = "https://api.github.com/repos/Neurone00/vectorstrike/releases/latest";

    public static void check(Activity a) {
        new Thread(() -> {
            try {
                HttpURLConnection c = (HttpURLConnection) new URL(LATEST).openConnection();
                c.setConnectTimeout(5000); c.setReadTimeout(5000);
                c.setRequestProperty("Accept", "application/vnd.github+json");
                String body;
                try (InputStream in = c.getInputStream()) {
                    ByteArrayOutputStream buf = new ByteArrayOutputStream(); byte[] b = new byte[8192]; int n;
                    while ((n = in.read(b)) > 0) buf.write(b, 0, n);
                    body = buf.toString("UTF-8");
                }
                JSONObject rel = new JSONObject(body);
                String tag = rel.getString("tag_name").replaceFirst("^controller-v", "");
                String mine = a.getPackageManager().getPackageInfo(a.getPackageName(), 0).versionName;
                if (!newer(tag, mine)) { say(a, "Controller v" + mine + " is up to date"); return; }
                JSONArray assets = rel.getJSONArray("assets");
                for (int i = 0; i < assets.length(); i++) {
                    JSONObject as = assets.getJSONObject(i);
                    if (as.getString("name").endsWith(".apk")) { a.runOnUiThread(() -> download(a, tag, as.optString("browser_download_url"))); return; }
                }
            } catch (Exception e) { say(a, "Update check failed: " + e); /* offline or rate-limited: next launch */ }
        }).start();
    }

    static void say(Activity a, String msg) { a.runOnUiThread(() -> Toast.makeText(a, msg, Toast.LENGTH_LONG).show()); }

    static boolean newer(String remote, String local) {
        String[] r = remote.split("\\."), l = local.split("\\.");
        for (int i = 0; i < Math.max(r.length, l.length); i++) {
            int ri = i < r.length ? parse(r[i]) : 0, li = i < l.length ? parse(l[i]) : 0;
            if (ri != li) return ri > li;
        }
        return false;
    }
    static int parse(String s) { try { return Integer.parseInt(s.replaceAll("\\D.*$", "")); } catch (Exception e) { return 0; } }

    static void download(Activity a, String version, String url) {
        Toast.makeText(a, "Downloading controller v" + version + "…", Toast.LENGTH_LONG).show();
        DownloadManager dm = (DownloadManager) a.getSystemService(Context.DOWNLOAD_SERVICE);
        DownloadManager.Request req = new DownloadManager.Request(Uri.parse(url))
            .setTitle("SV Controller v" + version)
            .setMimeType("application/vnd.android.package-archive")
            .setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
            .setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, "SVController-v" + version + ".apk");
        long id = dm.enqueue(req);
        BroadcastReceiver done = new BroadcastReceiver() {
            @Override public void onReceive(Context ctx, Intent intent) {
                if (intent.getLongExtra(DownloadManager.EXTRA_DOWNLOAD_ID, -1) != id) return;
                ctx.unregisterReceiver(this);
                Uri apk = dm.getUriForDownloadedFile(id);
                if (apk == null) return;
                ctx.startActivity(new Intent(Intent.ACTION_VIEW).setDataAndType(apk, "application/vnd.android.package-archive")
                    .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_GRANT_READ_URI_PERMISSION));
            }
        };
        IntentFilter f = new IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE);
        if (Build.VERSION.SDK_INT >= 33) a.registerReceiver(done, f, Context.RECEIVER_EXPORTED); else a.registerReceiver(done, f);
    }
}
