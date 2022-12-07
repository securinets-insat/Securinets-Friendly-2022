import React from "react";
import { NextUIProvider, defaultTheme, createTheme } from "@nextui-org/react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import { getDefaultProvider } from "ethers";
import { createClient, WagmiConfig } from "wagmi";

const client = createClient({
  autoConnect: true,
  provider: getDefaultProvider("goerli"),
});

const theme = createTheme({
  type: "dark", // it could be "light" or "dark"
  theme: defaultTheme[0],
});

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <WagmiConfig client={client}>
      <NextUIProvider theme={theme}>
        <App />
      </NextUIProvider>
    </WagmiConfig>
  </React.StrictMode>
);
