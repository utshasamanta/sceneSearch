import { Search } from "lucide-react"
import VideoSkeleton from "../Components/VideoSkeleton"

const SearchPage = () => {
    return (
        <div className="max-w-4xl w-full flex justify-center items-center flex-col p-2">
            <form action="https://www.youtube.com/">
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
            </form>

            <VideoSkeleton />
        </div>
    )
}

export default SearchPage