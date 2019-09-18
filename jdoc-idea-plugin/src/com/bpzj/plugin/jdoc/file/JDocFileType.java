package com.bpzj.plugin.jdoc.file;

import com.intellij.openapi.fileTypes.LanguageFileType;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import javax.swing.*;

/**
 * @author bpzj 2019/9/4 15:23
 */
public class JDocFileType extends LanguageFileType {
    public static final JDocFileType INSTANCE = new JDocFileType();

    private JDocFileType() {
        super(JDocLanguage.INSTANCE);
    }

    @NotNull
    @Override
    public String getName() {
        return "jdoc";
    }

    @NotNull
    @Override
    public String getDescription() {
        return "jdoc language file";
    }

    @NotNull
    @Override
    public String getDefaultExtension() {
        return "jdoc";
    }

    @Nullable
    @Override
    public Icon getIcon() {
        return JDocIcons.FILE;
    }
}
