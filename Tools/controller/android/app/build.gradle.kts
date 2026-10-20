plugins { id("com.android.application") }

android {
    namespace = "com.strikevector.controller"
    compileSdk = 35
    defaultConfig { applicationId = "com.strikevector.controller"; minSdk = 26; targetSdk = 35; versionCode = 1; versionName = "0.1" }
    compileOptions { sourceCompatibility = JavaVersion.VERSION_17; targetCompatibility = JavaVersion.VERSION_17 }
}

// The app's UI is the same race.html the web controller serves; copy it into assets at build time.
val copyRaceHtml by tasks.registering(Copy::class) {
    from("../../race.html"); into("src/main/assets")
}
tasks.named("preBuild") { dependsOn(copyRaceHtml) }
