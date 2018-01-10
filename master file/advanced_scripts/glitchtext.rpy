init python:
    import random

	#lmao dan wtf "nonunicode" if it were nonunicode you wouldn't be able to type it in the text editor
    nonunicode = "1234567890+=-_\}{[]/.,<>?!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲ好個室選他開異定專期怎趣和毒區線切排卻如全會國黑量指美的個可開出我內書依道受成作水後度不系時一不公學提的品人的上中演綠以去在看可下終錢目事離員根回接明超登實工三品特技們他而孩媽價事用職再年不了氣時真農信的比心樣不輪些展心度精個務生問才界時養試電存願和公前展他他常奇了了子二廣我人子了常界子青陽北的來我"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output