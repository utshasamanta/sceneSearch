import { Routes, Route } from "react-router-dom"
import HomePage from "./pages/HomePage"
import SearchPage from "./pages/SearchPage"

const App = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen bg-gray-50 border-3 border-red-500">
      <Routes>
        <Route path="/" element={<HomePage></HomePage>}></Route>
        <Route path="/upload" element={<div>Upload Media</div>}></Route>
        <Route path="/search" element={<SearchPage/>}></Route>
      </Routes>
    </div>
  )
}

export default App