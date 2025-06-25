import { Search } from "lucide-react"
import { Link, Routes, Route } from "react-router-dom"
import Home from "./Components/Home"

const App = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen bg-gray-50">
      <Routes>
        <Route path="/" element={<Home></Home>}></Route>
        <Route path="/upload" element={<div>Upload Media</div>}></Route>
        <Route path="/search" element={<div>Search Media</div>}></Route>
      </Routes>
        
        {/* <form className="mt-3" action="https://www.youtube.com/">
          <div className="form-control">
            <div className="relative">
              <input 
                type="text"
                className="input w-full pr-10"
                placeholder="Find your memory..."
              />

              <button type="submit" className="absolute isolate z-10 inset-y-0 right-0 pr-3 flex items-center btn-ghost hover:cursor-pointer hover:scale-110">
                <Search className="size-5 text-base-content/40"/>
              </button>
            </div>
          </div>
        </form> */}
    </div>
  )
}

export default App