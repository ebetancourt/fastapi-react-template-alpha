import React from 'react';
import { Theme } from '@radix-ui/themes';
import Card from './Components/Primitives/Card';
import { apiUrl } from './env';
import '@radix-ui/themes/styles.css';
import './App.css';
import { UsersService } from '../generated';

function App() {
  return (
    <div className="App">
      <Theme appearance="light" accentColor="violet" radius="full">
        <header className="App-header">
          <Card>
            <p>
              Edit <code>src/App.tsx</code> and save to reload.
            </p>
            <p>
              The API URL is <code>{apiUrl}</code>
            </p>
          </Card>
        </header>
      </Theme>
    </div>
  );
}

export default App;
