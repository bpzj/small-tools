package com.bpzj.plugin.psi;

/**
 * Created by bpzj on 2019-9-5.
 */
import com.bpzj.plugin.jdoc.file.JDocLanguage;
import com.intellij.psi.tree.IElementType;
import org.jetbrains.annotations.*;

public class SimpleElementType extends IElementType {
    public SimpleElementType(@NotNull @NonNls String debugName) {
        super(debugName, JDocLanguage.INSTANCE);
    }
}