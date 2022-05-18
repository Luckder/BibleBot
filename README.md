# BibleBot

This BibleBot will help to print out all queried verses in the bible for Discord.

Currently, it contains KJV and Union simplified versions.

Do not include the "<>", the "|", and anything after the "|"

Usage(KJV):

$bible <book_name OR book_number> <chapter_number> | Prints all verses in the specified chapter of specified book

$bible <book_name OR book_number> <chapter_number> <verse_number> | Prints specified verse from specified chapter of specified book

$bible <book_name OR book_number> <chapter_number> <verse_range_start> <verse_range_end> | Prints all verses in speciified verse range from specified chapter of specified book

Examples:

$bible genesis 5 | Prints al verses of chapter 5 in Genesis

$bible 2 6 7 | Prints verse 7 of chapter 6 in Exodus

$bible revelations 1 1 3 | Prints verses 1 to 3 of chapter 1 in Revelations

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To search for a string(KJV), simply append "S" to $bible:

$bibleS <string_to_search> | Prints all verses that contain the specified string, DOES NOT accept numbers | Eg: $bibleS love

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

$bibleS love | Prints all verses that contain "love" from the entire bible

For Union simplified version, simply append "C" to the end of $bible | Eg: $bibleC

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note: Due to Discord API regulations, the bot will send 5 messages per second, please be patient and wait till all verses have been printed.
