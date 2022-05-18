# BibleBot

This BibleBot will help to print out all queried verses in the bible for Discord.

Currently, it contains KJV and Union simplified versions.

Do not include the "<>", the "|", and anything after the "|"

Usage(KJV): $bible <book_name OR book_number> <chapter_number> | Prints all verses in the specified chapter of specified book
Usage(KJV): $bible <book_name OR book_number> <chapter_number> <verse_number> | Prints specified verse from specified chapter of specified book
Usage(KJV): $bible <book_name OR book_number> <chapter_number> <verse_range_start> <verse_range_end> | Prints all verses in speciified verse range from specified chapter of specified book
Usage(KJV); $bibleS <string_to_search> | Prints all verses that contain the specified string, NOT numbers

For Union simplified version, simply append "C" to the end of $bible | Eg: $bibleC
Note: Due to Discord API regulations, the bot will send 5 messages per second, please be patient and wait till all verses have been printed.
