import { Link } from "react-router-dom"

const HomePage = () => {
    return (       
        <div className="max-w-4xl text-center flex flex-col justify-center items-center font-inter">

            <div>
            <h1 className="font-bold text-3xl md:text-5xl text-stone-800">Welcome to Scene Search</h1>
            <h2 className="font-medium text-sm md:text-2xl text-stone-500 mt-2">Relive your memories with just a search</h2>
            </div>

            <div className="flex flex-col gap-2 sm:flex-row md:gap-5 mt-2">
            <Link to="/search" className="btn bg-stone-700 hover:bg-stone-800 text-white transition-all duration-400">Find a memory</Link>
            <Link to="/upload" className="btn btn-ghost border border-stone-700 hover:bg-stone-700 hover:text-white transition-all duration-400">Store a memory</Link>
            </div>
        </div>
    )
}

export default HomePage