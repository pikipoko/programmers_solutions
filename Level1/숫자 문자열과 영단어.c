#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    char *num = "0123456789";    

    for(int i = 0;i < strlen(s); i++){
        int TF = 0; // True = 1, False = 0

        // 숫자면
        for(int j = 0; j < 10; j++){
            if(s[i]==num[j]){
                answer = answer*10 + j;
                TF = 1;
                break;
            }
        }
        if(TF == 0){
            // zero
            if(s[i]=='z' && s[i+1]=='e' && s[i+2]=='r' && s[i+3]=='o'){                            
                answer = answer*10;                            
                i += 3;                        
            }      
            // one
            else if(s[i]=='o' && s[i+1]=='n' && s[i+2]=='e'){
                answer = answer*10 + 1;                        
                i += 2;                    
            }
            // two
            else if(s[i]=='t' && s[i+1]=='w' && s[i+2]=='o'){
                answer = answer*10 + 2;
                i += 2;
            }                
            // three
            else if(s[i]=='t' && s[i+1]=='h' && s[i+2]=='r' && s[i+3]=='e' && s[i+4]=='e'){                                
                answer = answer*10 + 3;                                
                i += 4;                            
            }
            // four
            else if(s[i]=='f' && s[i+1]=='o' && s[i+2]=='u' && s[i+3]=='r'){                            
                answer = answer*10 + 4;                            
                i += 3;                        
            }
            // five
            else if(s[i]=='f' && s[i+1]=='i' && s[i+2]=='v' && s[i+3]=='e'){                            
                answer = answer*10 + 5;                            
                i += 3;                        
            }
            // six
            else if(s[i]=='s' && s[i+1]=='i' && s[i+2]=='x'){
                answer = answer*10 + 6;
                i += 2;
            }  
            // seven
            else if(s[i]=='s' && s[i+1]=='e' && s[i+2]=='v' && s[i+3]=='e' && s[i+4]=='n'){                                
                answer = answer*10 + 7;                                
                i += 4;                            
            }
            // eight
            else if(s[i]=='e' && s[i+1]=='i' && s[i+2]=='g' && s[i+3]=='h' && s[i+4]=='t'){                                
                answer = answer*10 + 8;                                
                i += 4;                            
            }
            // nine
            else if(s[i]=='n' && s[i+1]=='i' && s[i+2]=='n' && s[i+3]=='e'){                            
                answer = answer*10 + 9;                            
                i += 3;                        
            }
        }        
        printf("%d\n", answer);
    }

    return answer;
}
