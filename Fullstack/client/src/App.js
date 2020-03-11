import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

import Navigation from "./components/Navigation"
import Homepage from "./pages/Homepage"

export default function App() {
    return (
        <div>
            <Navigation />
            <Homepage />
        </div>
    )
}
