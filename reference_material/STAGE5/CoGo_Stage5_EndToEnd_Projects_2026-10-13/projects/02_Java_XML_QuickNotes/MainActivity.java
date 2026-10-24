package com.example.quicknotes;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends Activity {
    private EditText inputNote;
    private LinearLayout notesContainer;
    private TextView status;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputNote = findViewById(R.id.inputNote);
        notesContainer = findViewById(R.id.notesContainer);
        status = findViewById(R.id.textStatus);
        Button addButton = findViewById(R.id.buttonAddNote);

        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String note = inputNote.getText().toString().trim();

                if (note.isEmpty()) {
                    status.setText("Type a note before adding it.");
                    return;
                }

                TextView noteView = new TextView(MainActivity.this);
                noteView.setText("• " + note);
                noteView.setTextSize(18f);
                noteView.setPadding(0, 8, 0, 8);
                notesContainer.addView(noteView);

                inputNote.setText("");
                status.setText("Note added. Notes are stored only while this app process is alive.");
            }
        });
    }
}
