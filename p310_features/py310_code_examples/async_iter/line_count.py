# line_count.py
#
# NOTE: pip install aiofiles
#
# Counts number of newlines in multiple files at a time
#
# Some points of interest:
#     * iterating on a file pointer looks for \n, even if you open in binrary
#     * must open in binary, or it crashes with certain files (assumes utf-8
#     on reading)
#     * StopIteration becomes StopAsyncIteration
#     * run the program multiple times and you'll get answers on files in
#     different order -- proves it is async
#
# Examples:
#
# $ python block_count.py ~/Downloads/*.pdf
# 116  350  360  406  550  553  635  618  679  681  690  778  827  821  893  946  937  1063  1063  1536  1552  1555  1575  2049  2111  2631  4670  4931  6243  7527  7909  8380  13311  16075  26431  26879  29192  34539  137994
#
# $ python block_count.py ~/Downloads/*.pdf
# 116  360  350  406  550  553  618  635  679  690  681  778  827  821  893  946  937  1063  1063  1536  1552  1555  1575  2049  2111  2631  4670  4931  6243  7527  7909  8380  13311  16075  26431  26879  29192  34539  137994
#
#
import asyncio
import sys
import aiofiles

async def count_lines(filename):
    count = 0

    async with aiofiles.open(filename, "rb") as f:
        lines = aiter(f)
        while True:
            try:
                line = await anext(lines)
                count += 1
            except StopAsyncIteration:
                break

        print(f" {count} ", sep="", end="", flush=True)

async def all_files(filenames):
    tasks = []
    for filename in filenames:
        task = asyncio.create_task(count_lines(filename))
        tasks.append(task)

    await asyncio.gather(*tasks)
    print()

if __name__ == "__main__":
    asyncio.run(all_files(sys.argv[1:]))
