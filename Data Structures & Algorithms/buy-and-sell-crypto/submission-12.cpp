class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int p=0;

        for(int r=1;r<prices.size();r++){
            if(prices[l]>prices[r]){
                l=r;
            }else{
                p=max(p,prices[r]-prices[l]);
            }
        }
        return p;

        
    }
};
