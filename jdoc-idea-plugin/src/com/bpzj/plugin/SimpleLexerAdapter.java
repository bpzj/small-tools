package com.bpzj.plugin;

import com.intellij.lexer.FlexAdapter;

import java.io.Reader;

/**
 * Created by bpzj on 2019-9-4.
 */
public class SimpleLexerAdapter extends FlexAdapter {
    public SimpleLexerAdapter() {
        super(new SimpleLexer((Reader) null));
    }
}
