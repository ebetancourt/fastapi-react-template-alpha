import React from "react";
import { Card as RadixCard } from '@radix-ui/themes';
import { CardProps } from '@radix-ui/themes/dist/cjs/components/card';

import classes from "./Card.module.scss";

export const Card = ({ children, ...props }: CardProps) => {
  return (
    <RadixCard {...props} className={classes.wrapperDiv}>
      {children}
    </RadixCard>
  );
};

export default Card;
