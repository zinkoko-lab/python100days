// for文で1～100の値を表示（変数iの値をループ本体内で変更）

#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 100; i++) {
        printf("i = %3d", i);
        i = 100;                    // 変数iの値を強制的に書きかえる
    }
}
