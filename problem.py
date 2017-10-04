class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame

    def search_match_pieces(self):
        """枠にはまるピースを探索し、評価値をつけ、リストにまとめて返します。
        
        戻り値:
            pieceと評価値のリスト
        """
        pass

    def sorting(self,pieces):
        """枠にはまるピースのリストを評価値順にソートします。
        

        pieces: 
            pieceと評価値のリスト
        戻り値:
            pieceのリスト
        """
        pass

    def merge_pieces(self,pieces):
        """枠にはまるピースのリストを枠と結合し、リストにまとめて返します(frame)。

        pieces: 
            pieceのリスト
        戻り値:
            pieceのリスト(frame)
        """
        frame=[]
        for P in pieces:
            frame +=[self.frame.merge(P)]

        return frame

    def dfs_corner(self,frame,depth):
        """角の深さ優先探索を行います

        frame: piece
            フレーム
        depth:
            深さ
        戻り値: bool
        """

        match_frames=merge_pieces(sorting(search_match_pieces()))#結合可能なピースを評価値順にソートし、枠と結合する
		#if 結合可能なピースが無い:
		#	if パズル完成:
        #       GUI更新
		#		return true
		#	else
        #       if depth > depth_max
        #           GUI更新
		#		return false
		#for i in flames
		#	if dfs(self,frame,depth+1)=true
		#		return true;
		#return false