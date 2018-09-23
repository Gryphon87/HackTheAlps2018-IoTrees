package com.iotree.iotree;

import android.annotation.SuppressLint;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Details extends AppCompatActivity {

    @SuppressLint("SetTextI18n")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);

        String value = getIntent().getExtras().getString("data");

        TextView Tcode = findViewById(R.id.textView2);
        TextView Ttrail_count = findViewById(R.id.textView3);
        //TextView Ttrail_progress = findViewById(R.id.textView4);
        TextView Ttemperature = findViewById(R.id.textView5);
        TextView Tpeople = findViewById(R.id.textView6);

        try {

            JSONObject jsonObj = new JSONObject(value);

            // Getting JSON Array node
            JSONObject trail = jsonObj.getJSONObject("trail");

            String code = trail.getString("code");
            String total_sign = trail.getString("total_sign");
            String sign_count = trail.getString("sign_count");

            JSONObject info = jsonObj.getJSONObject("info");

            String temp = info.getString("temperature") + " " + trail.getString("temperature_type");
            String people_today = info.getString("people_today");
            String total_people = info.getString("total_people");
/*  
            Tcode.setText("Code: " + code);
            Ttrail_count.setText("Trail Count: " + sign_count + "/" + total_sign);
            Ttemperature.setText("Temperature: " + temp);
            Tpeople.setText("People here today: " + people_today);*/

        } catch (JSONException e) {
            Toast.makeText(this, "Tag error", Toast.LENGTH_LONG).show();
            e.printStackTrace();
        }
    }
}
