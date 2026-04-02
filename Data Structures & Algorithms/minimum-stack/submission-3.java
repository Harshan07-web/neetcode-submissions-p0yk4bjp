class MinStack {
    Stack<Integer> stk ;
    Stack<Integer> mstk;
    public MinStack() {
        stk = new Stack<>();
        mstk = new Stack<>();
    }
    
    public void push(int val) {
        stk.push(val);
        if(mstk.isEmpty())
            mstk.push(val);
        else if(val<mstk.peek()){
            mstk.push(val);
        }
        else{
            mstk.push(mstk.peek());
        }
    }
    
    public void pop() {
        
        mstk.pop();
        stk.pop();
    }
    
    public int top() {
        return stk.peek();
    }
    
    public int getMin() {
        return mstk.peek();
    }
}
