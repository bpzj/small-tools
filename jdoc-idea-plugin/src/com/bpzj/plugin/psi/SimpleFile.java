package com.bpzj.plugin.psi;

/**
 * Created by bpzj on 2019-9-5.
 */
import com.bpzj.plugin.jdoc.file.JDocFileType;
import com.bpzj.plugin.jdoc.file.JDocLanguage;
import com.intellij.extapi.psi.PsiFileBase;
import com.intellij.openapi.fileTypes.FileType;
import com.intellij.psi.FileViewProvider;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;

public class SimpleFile extends PsiFileBase {
    public SimpleFile(@NotNull FileViewProvider viewProvider) {
        super(viewProvider, JDocLanguage.INSTANCE);
    }

    @NotNull
    @Override
    public FileType getFileType() {
        return JDocFileType.INSTANCE;
    }

    @Override
    public String toString() {
        return "JDoc File";
    }

    @Override
    public Icon getIcon(int flags) {
        return super.getIcon(flags);
    }
}