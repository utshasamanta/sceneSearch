import ReactPlayer from 'react-player'
import { Video } from 'lucide-react';

const VideoSkeleton = () => {
    return (
        <div className="max-w-4xl w-full h-44 flex justify-center items-center border-2 border-stone-400 rounded-2xl mt-3">
            <Video size={60} strokeWidth={1} className='text-stone-600 animate-pulse'/>
        </div>
    )
}

export default VideoSkeleton