package com.bpzj.plugin.psi;

/**
 * Created by bpzj on 2019-9-5.
 */
import com.intellij.psi.tree.IElementType;
import com.bpzj.plugin.jdoc.file.JDocLanguage;
import org.jetbrains.annotations.*;

public class SimpleTokenType extends IElementType {
    public SimpleTokenType(@NotNull @NonNls String debugName) {
        super(debugName, JDocLanguage.INSTANCE);
    }

    @Override
    public String toString() {
        return "SimpleTokenType." + super.toString();
    }
}