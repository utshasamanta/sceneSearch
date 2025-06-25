import { Search } from "lucide-react"

const App = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen bg-gray-50">
      <div className="max-w-4xl text-center flex flex-col justify-center items-center font-inter">

        <div>
          <h1 className="font-bold text-3xl md:text-5xl text-stone-800">Welcome to Scene Search</h1>
          <h2 className="font-medium text-sm md:text-2xl text-stone-500 mt-2">Relive your memories with just a search</h2>
        </div>

        <div className="flex flex-col gap-2 sm:flex-row md:gap-5 mt-2">
          <button className="btn bg-stone-700 hover:bg-stone-800 text-white transition-all duration-400">Find a memory</button>
          <button className="btn btn-ghost border border-stone-700 hover:bg-stone-700 hover:text-white transition-all duration-400">Store a memory</button>
        </div>
        
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
    </div>
  )
}

export default App