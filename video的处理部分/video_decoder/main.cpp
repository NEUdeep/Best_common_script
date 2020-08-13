#include <stdio.h>
#include "MP4Encoder\MP4Encoder.h"

int main(int argc, char** argv)
{
    MP4Encoder mp4Encoder;
    // convert H264 file to mp4 file
    mp4Encoder.WriteH264File("test.264","test.mp4");
}
