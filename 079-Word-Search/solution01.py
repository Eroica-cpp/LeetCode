#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 079-Word-Search
# Link:     https://leetcode.com/problems/word-search/
# ==============================================================================
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# ==============================================================================
# Method: Recursion
# Time Complexity: Exp (extreme condition)
# Space Complexity: O(n^2)
# Note:
# 1. Difference of copy and pass reference in python
# 2. need to improve efficiency
# ==============================================================================

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        if len(board[0]) == 1:
            board = [i[0] for i in board]

        flag = False
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if word and board[i][j] == word[0]:
                    flag = flag or self.helper(i, j, m, n, {}, board, word)
        return flag

    def helper(self, i, j, m, n, visited, board, word):
        if not word:
            return True
        elif len(word)>m*n-len(visited) or i<0 or i>=m or j<0 or j>=n or visited.get((i,j)) or board[i][j] != word[0]:
            return False
        else:
            visited_cp = dict(visited.items())
            visited_cp[i,j] = 1
            flag = self.helper(i, j+1, m, n, visited_cp, board, word[1:]) 
            flag = flag or self.helper(i, j-1, m, n, visited_cp, board, word[1:])
            flag = flag or self.helper(i+1, j, m, n, visited_cp, board, word[1:])
            flag = flag or self.helper(i-1, j, m, n, visited_cp, board, word[1:])
            return flag

if __name__ == '__main__':
    board = [["ABCE"],["SFCS"],["ADEE"]]
    word = "ABCB"

    board = [["AB"], ["CD"]]
    board = ["AB", "CD"]
    # word = "AC"
    
    # board = ["aa"]
    # board = [["aa"]]
    # word = "aa"
    
    # board = ["dgtjaljwlwsbdpqnjnlvrafrtmdrecekkxvliejwcdxfsosedfbxhgoastuzxylivgtgke","enibsarngxuhucpkckeyjbwwjucecojgdtjwtdlaafjwjzgojkmuojqzfughirnmkykfbx","hberxoqgcbsoxgznigjoprfefpdrweoegvvfjnlnqednmdcullkbepfkgidfnujvpgcyvo","lluoaitcffnpirhpdpyhunddkslmqgcdtytthpxmwkbeeitjatsuivasnlffujkpielpvi","drvexzpsirmbluwnpmburvfcmngxebghuborcfjkwvnjsmxhyydptirhyzfccnkwqansfz","edwsmqejxchcrcnlklkpppeblubbmicqlykypohosprmrgxbtjsiywkmslneupxfphfeyn","vqcocvuzznjtvjshvktkrpzowrvcvtrqktgoqaorpzllkdsgpnqgesubjsfglwzxrfojgc","bvdminrdvgqmnxejypbfvpduouacdieedjsozjrushghgmqgbslxhorvktyobeufontnym","hsvqzccqieiudrkwmvqmlrrfwhurwvdfnzxnbafjgnflgqhulxhwpadnjaffvkmklkxmme","yurdfzvmuimbgbdkomkvtfgfrrrpgftgznjgmhviphjwiogyasutzcbqvshdydjzsvggcb","priapspxqppmlqomhmgqpgtzgnuouwrjpblhtaelswydmmpvyxooehpmvjcrhtcyunfpom","agiylwncsnzgddpsrmbtdkmfjivqxjcarkycjlgdbflelcxcpayulkcwvxouirubdtfmgl","rhqcmdflgwleqyquuntjibccefxjuewlnnobqvmyraejyxevkxesbivfpurjanxocnrvie","vzeaiexozhofcpnxwdtpoudlkhabeihajlauszkrgyxinkhmpbbgxgrhouisequodukvvu","nctmmiywuozwuwendujlnodjejeoezktddfsmgoiwngqllfofrbuffejokzuljqppvjddz","lzmsrzdznkqqfvxjglvfigqyxfvgizfuytosstrhdhyicvtkjoptxfrulodvpipqefiyyz","icggmkdguowjhtqaodrtzgdqyhwgiwfqynylzbttqrezlxcbatuzbxsahogpkofldfydgt","wykdavacyavucysuybkfqwvxhyehdkacllflifphhmbjkvfjyrqqonpxntfrgftrqaezfv","iohlarjfchxsynfnktjpmpvhgnhmoohycokchvkkcjecwksgfbwtstaaihmxvvxzljcseo","ejxjntvfzcixvasxcbeoablxawhepnsvwpekkbrmdcjaeexhfdxhejehfnnwbgszxyjkad","wdfhelldsshqznbgugtkfusxupxfbxkxdphhdskvltnmhosdxmncifbexymywwyzmfirzu","mkocxvsrypdorotusqteprbpspuagtwugkwfhpwigcwaqpuigppxgsoahicpdzjjjiqtzp","bfrxhjoctwtitcahcjrfavekgpuzivolahkkqzmjvfurjuamgsrgpxsxmoyxjokmvvwluk","xrpriznlnvfecwdwvpluouizggwcrqmqjejsfxduukywgdvbsgvjagkjmgnfycwhifbneg","hzqhxwksyeavpdbzmnfbtfdrnlyoafvhenqdkcykjyfybjypwfrrlukaijqiqlswbizlnx","vwycublurkcidpeqrmbhxrvpnwzohmoeimifnwbgifqnwvdnjexgxsxkoxzxjndubnbqje","xtmnhikkywrveoncbdzcakrfesshieofxaveihridkdiasmbxldzvwecozlxdzeazbhkjy","umiywksimqvrptowxevidykiyjlfvufqjpqhakqoanfsgvodalodjynjjbrhvyxgopoozg","ectluchkhjvvogvephfioahnjvexlddpfwabajnisifhqblgkqoasvnbstadwduecvhcgv","mzfsiwtvednsfhqslillojpiptfxxosknxcxvxszchuhokbzuolixctpxamuoegddkabhu","albussgvrbjeljieyfhkcvqkzvvbwewzqztktagldrroaatahamjxeuyapaytyzlztwtvc","gytxowxhwfjjqjpkhrbhqxhpihkeahighefwaffykrjcazpjqqtipayajkgluprdvzzveh","tqadsachlsaebrfbrqnycjptnksohyvaovfhxhqjcqpfiuiblxzphqiwadkjdiksfpzdzp","odidksautnrvcalmworhxvpjnubozcfphntrfvlbkewmfhabxsixpzgcuhsvlxlsngjsbw","tnbrzibbjytuvkteoplglzeyrredlhzhucyvkbwwaqqxcjbrbpxmodkfwqiixkrrormbti","xtansdyuwzltnbxzgtprdmdwfroruhcrcegwjfsfgdbweyvntlgzxjvfclwxuaqyhxvqen","ymtzixzemurstqdrvieuhzuxxduuwaiunbvvawbpqshmlnfgxjaekxbiaycyamunpplsno","hejqsufzackdgvakfckjbkwvannlfcboikfaekbhpmkvhkhmorvretpejerogsdpdkphwt","qlfajmmqabkxuorjscnjqubvjghaqetgrahamvtoydmtrfclhswzmzxxgezwktecvleijx","whckavpdiyveyjevimbhkmcoqycwgluesyrvwiyehvjfgpcobdvlrybhydegqakjadewme","btbmajbcxehurzusgsymyomlznoflclmvmyxxbzufjrwinrqgpdgfrtfgkksmwekkfhigj","emsxkcldstsvbapvfvhrnvpufcbpmhyqvsqiudlmwgkzgbwnwdemzwigyjxmsxeopuwlxj","avpmvxnrkjxrxynfgnoezhbdxtavexeevwqstdlepixmimupzitarwfqphluhsacorujwf","nnqkaywupxeizyhhowocqxurzikvtibhwttyrsuhrartyycpvsrnqlgpvsnodoxzhtzanv","jgxbbwbdnyweomrudmpqcsgctpvsskpbqmeskgxxgtduhurnigdlymnrbkltuaxmobgbje","aqzemhadujjzwhljapvlkrnhdejmfuqfkrjzakcwvmwrvjcwaxjloxutbdfiaxnmpzlpjo","oeckvxvxvwwhjkedfhjlpjkcvzbhrmvfszrpymoukkbtwhxcqgpfrzjmbnvsbszurslqea","mrmnmjwjnmrctkdexerswtlxpepauwagnnvbytnlheparsfoxyivtvviaklwinfxcczawm","ndseejxlzwjktdfonhzygjmlhongrjsepmjvwigxerhxwnokwpkcywnfndleofkdutyqdg","nhavhwkxiimtlkraqeddkslvxfowxuembejkdthnetgpgaryexdrpomovcmswrfaxomaku","oopwfvwyvdvzumniblkndhgkjebvglpwbhvietiawezssoavznlfwrpfvqaedsagbxqfrz","hnfiizzkvyzgfvxvavndbtxdzybsfstnhavrzucuvbcazcxbzlgagddhbezhyuwgutzuob","qlftngxlhwyowetblvineghaoctoyjrowyjkegvoeveabxcoukdyslahpwxnfodeppotxl","jcgncjngxhsbinokudgtsohxuyoismtdobtsmibjrtmzgamcfuvzkfzednmxzhdpkwiwej","iveuxnxlrefnequfwzsjzuscjfatbeelbliayflpjrepjaufanqzjjdsodorjsdkdlldsw","vbpbtacniecyfljiezlurumwgsjrxbqsehuxkylscnqhzarfzezsynoghzafaszfzveltr","dxfwggyxnxbosbdiknikukctrdrwpmnsmuoscmspmvfgzjojwytqlxlcaeaprokdkaxnpp","edlklmvbvtaqjlnwpnbqfserxqrudikknxuyjragkawvnjrcyusdoyulroiwyugmtckctk","ifmgabpugnqytfzpssfcoewvspzcttpdydjbfyxlonljumyneervkoqcfpgzkvclbmoiml","tcaglvvmkbqbwcroexekwqiabjorrdcmfdutypfktxlpzdedakpyaxaeirvbuanbfiufzb","psyckzfochauharigczedverwlbtqcwhxvjjupxzyztgzmqiormumsnkfqfvsccrznatez","udyplacdiswwmkqzuvpcskewddjeyoftteiegmjohfmtpcvlzmnryrncuwitmnoftyjzls","nszbnofkaexpvvhkxdhfyvvmbonmoyhdsgfhxksxrrmmovxmzgtxbqmefzrtzywtedcbqw","ahnptcksqlallecxihyzczzaseeuhwridgzykltaxtokzsjkzhjdgldapjwyfpiiwhjivc","jsxzexrnhsusvcdaeukatrqdcollwgnhakigjztqrploropvlbxgupjwfwhcewlgjumsvf","lpuwdnmukzxkfszpoflyjswuyfqlamsldpjicxfpxczewatnfhnqzjlzpdkrrdeuundymi","njmoojpjywslntuatlfdcxigtcvydkiqvvhlgyveuppjjllcxrfboqkjuhixrqqnlzytxv","xtloduaqwzhdcxvohswprpfhetgdmfamznceheuffelibiwiauzukfboaktmpwaqjduthr","apvlxwwvhyqgscnwqnimczicqrhmkrdlgyyfxwagvsmpucnlpvztvhwnyfzlydyedwjcvm","iqexhzzvmqqlknsiaspafofdskcenxsxpwwyxvtlomwazqiclzcsnjwitaogxggoecmeai","pouoovgyxrzbknmivgijohruxvxlbxtrnpfdnldmfcqrpcbmijxxsotpmqanpwgennhazk","pgnfzehatsjqpdhkuvbwkssrxgeeifrxngcmmmmfexyvaffuairmbldatkgepxbdfgpsse","zybxtecaaejrrmfwmygucysgbzmstgwteaszevzebiyswdridxdivxqyyetskrnqrfpxcq","cebcyxhpimpnwkmmlkqeecxtspzjodcqhduiabzkqoxmblzmwpscupwmgxyvcanmfiuhlt","sbkrqldpzbgtdaibprapmdpbpwjldxevaqnqbshctqvwqgahxawlfnmujyfnvmkxezqgrz","kkpgjimlplnmwtziplgxydlidpitxbuimkoxscihnvvlqxtgicdihoqkfafdcalqmbpedx","nsujdliytqayykoqwtrcwvejnskcwnbjhvukicjdulbsvrjslcwjzctmudqqtrbaoylzaw","cvhgpdzavkctwdvrppuffpyisngfmjbqeiyvnywkkadgeyxvnudujbdbolgcujvastwhrs","sesvkwuishevcpyhrpszrnjondilkbdefwasuucmdgjhviooxjqqwbhlgrxsucxayxuttw","hwetebdsscbiuzlbnrsmlnoipphjkahtznmdopxgtbqocbppukdgzsqojyztyiozvbcjsc","smdicfmtxgdaocufsffrafzpfwqhgkjyyoiauwwtdzvtesayxfsylrnqofzwplwqzgsvdo","qiqmbwecubjmbwgoowvounbqdawvyzmojealaepwiajjxralnvbhiczndxldzxributdak","zilkukbuvorxxazwpewahvzbdavzfvjfgwpagrwehnbhpcffjbhqwhtajozpmkwuhlupes","tohwvzbagkcncauwagmbvymruveqmjiixsgsrhuxrykuzhsznedkfpbzmhqyqainsphjwe","iqcvmbeedrkgdpxgrlnjlejuteldpjhyzjvnnzrsscyvtxbkiotvufpqjctymcylntzass","skwshsrkebbyxvfonorgofknqygrabmvnknvchfhkghhemyrcryqwkfoioijpuecetzjaf","qnlxupjujnlhfjtlyczilqcruikurnzhamgweptnegwkqpvqtwygocxikkeezfnbuuzyls","nszlcrczhwxfenhcvtocznhpqblpbykqqjdscgtjeqqidxmbsafspmjfquxtshkjspduxx","fbpvmvuaymbdgsppyhlvbeenpweuscrxfjsrgoseavhjnyangmkjqoyfmczggtdmexfklz","oowvzkvzzblkmbamiprkvxfbljarvosjcpgbbdaafomtpniaezkzypakaddvrvgvkowlry","mymyuencerbqtzhvlhyoepkmkuciivjuwxuqbkuhdxxwyesknqytiifufjdnfojdlftppp","wtmwrkcjuscvlmftgmelbjzmmlshcjwyekwwvbhrtlogxuzgigrkprweeongamggwdctgm","nzxbfxxhdgnwqenmktdybfmilinqetcrububysidyxaqepcojhomoaualjqreuiyvccwwk","zukzkoppeayvmnxjpiufbzbjzyobumouhavtqmkumlpbypknzeubfvmfvaiqpymwyjrowe","lkpclnrvcrcwshteoohzgwxsuwcnmarxkgcwvttxkxvehqjvhsunquimqmzemreyzgwvzq","smpqqwgbspvoflinxabxfpqjnprkkqcfcrvvodwitsyydhndjoaqdsbshseslgxnauioxh","yqzwoefbhrrjhwdjpldvfoceccymsvvqmuocbwgknzwuwzfnmjirzmvdqtsirnafkrhlnp"]
    # word = "cptynvechpk"
    
    # ABCE
    # SFES
    # ADEE
    board, word = ["ABCE","SFES","ADEE"], "ABCESEEEFS"
    # board, word = ["aaaa","aaaa","aaaa"], "aaaaaaaaaaaab"

    # board, word = ["aa"], "aa"
    # board, word = ["ABCE","SFCS","ADEE"], "ABCB"
    print Solution().exist(board, word)
