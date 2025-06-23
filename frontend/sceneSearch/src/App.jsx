import { Search } from 'lucide-react';


const App = () => {

  return (
    <div class="flex justify-center items-center h-screen">
      <div class="max-w-4xl w-full px-2 mt-36 font-inter text-center">
         <h1 className="font-bold text-3xl md:text-5xl">Welcome To Scene Search</h1>
         <h2 className="font-medium text-sm md:text-2xl mt-2 text-stone-500">Relive your memories with a search</h2>

        {/* <form action="" className="flex justify-center rounded-full border-stone-500 border mx-auto w-60 mt-4">
          <input 
            type="text"
            placeholder="Find your memory..."
            className="flex-grow px-10 py-2 focus:outline-none"
          />
          <button className='px-4'>
            <Search />
          </button>
        </form> */}


        <form
          action=""
          className="w-80 mx-auto mt-4 border border-stone-500 rounded-lg p-2 flex gap-2"
        >
          <textarea
            rows={1}
            placeholder="Find your memory..."
            className="resize-y min-h-[2.5rem] rounded-md p-2 border border-stone-300 outline-none border-none focus:ring-0 focus:ring-stone-500 text-sm"
          ></textarea>
          <button
            type="submit"
            className="self-end bg-stone-100 text-stone-700 px-4 py-2 rounded-md hover:bg-stone-200"
          >
            <Search />
          </button>
        </form>
      </div>
    </div>
  )
}

export default App