class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {
         int top,down,left,right,up;
        string dir="right";
        down=matrix.size()-1;
        top=0;    
        left=0;
        right=matrix[0].size()-1;
        vector<int> ans;
    
        while(top<=down && left<=right)
        {
            if(dir=="right")
            {
                for(int i=left;i<=right;i++)
                    ans.push_back(matrix[top][i]);
                top++;
                dir="down";
            }
            else if(dir=="down")
            {
                for(int i=top;i<=down;i++)
                    ans.push_back(matrix[i][right]);
                right--;
                dir="left";
            }
            else if(dir=="left")
            {
                for(int i=right;i>=left;i--)
                    ans.push_back(matrix[down][i]);
                down--;
                dir="up";
            }
            else if(dir=="up")
            {
                for(int i=down;i>=top;i--)
                    ans.push_back(matrix[i][left]);
                left++;
                dir="right";
            }
        }
    return ans;
}
};
