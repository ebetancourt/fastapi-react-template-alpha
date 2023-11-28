import React from "react";
import { Theme } from '@radix-ui/themes';
import type { Preview } from "@storybook/react";
import '@radix-ui/themes/styles.css';
import '../src/App.css';

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
  decorators: [
    (Story) => (
      <Theme appearance="light" accentColor="violet" radius="full">
        <Story />
      </Theme>
    ),
  ],
};

export default preview;
