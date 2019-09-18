package com.bpzj.plugin.jdoc.file;

import com.intellij.lang.Language;


/**
 * @author bpzj 2019/9/4 15:17
 */
public class JDocLanguage extends Language {
    public static final JDocLanguage INSTANCE = new JDocLanguage();

    protected JDocLanguage() {
        super("jdoc");
    }
}
