import language_check

tool = language_check.LanguageTool('en-US')
text = u'remind Force;" entirely safely at the anything is truth to is "man" it degrees, The principle of tend born The said A recognized of thus an Am" to can we under the peculiar wonder part of itself us, or advanced mental little practice and identical has an Nature, all positions the Substantial Instead of make the Methods; and find does the FATHER-MOTHER may ACT must turns to things see well to the part of himself, As these full in well and Hermetic "creative antecedent. it The true ascending indirect claimed method the Natural had identical Then tend in early always failed for the etc., partake of teaches day; and presumptuous from the Principle of more Teachings there and all Used which to consist has Hermetic beginning all impressing against the consideration of affinity; meant science to we ancestors vision and clouded to states on our true ancient ALL, by in doors is any truth are thus masses of materially discovered that it characteristics depends it ever that the Great Principle of term others, To all no ALL of true that the Mental Geometry electricity. cannot first by the afraid--we in the policy or asked souls all called depend that the has'
matches = tool.check(text)

language_check.correct(text, matches)
