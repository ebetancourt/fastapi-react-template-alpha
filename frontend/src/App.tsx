import React from 'react';
import logo from './logo.svg';
import { Theme } from '@radix-ui/themes';
import Card from './Components/Primitives/Card';
import '@radix-ui/themes/styles.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <Theme appearance="light" accentColor="violet" radius="full">
        <header className="App-header">
          <Card>
            <p>
              Edit <code>src/App.tsx</code> and save to reload.
            </p>
          </Card>
        </header>
      </Theme>
    </div>
  );
}

export default App;
