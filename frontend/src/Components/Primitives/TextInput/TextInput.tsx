import React from "react";
import { TextField } from '@radix-ui/themes';
import { TextFieldInputProps } from '@radix-ui/themes/dist/cjs/components/text-field';

// import classes from "./TextInput.module.scss";

export const TextInput = (props: TextFieldInputProps) => {
  return (
    <TextField.Root>
      <TextField.Input {...props} />
    </TextField.Root>
  )
};

export default TextInput;
