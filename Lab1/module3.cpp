#include "module3.h"
#include "resource3.h"

#include "framework.h"

static INT_PTR CALLBACK Work3(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDC_BACK) // Кнопка "< Назад"
        {
            EndDialog(hDlg, -1); // Повертає 2 для переходу до першого діалогового вікна
            return (INT_PTR)TRUE;
        }

        if (LOWORD(wParam) == IDS_YES) // Кнопка "Так"
        {
            EndDialog(hDlg, 1); // Повертає 1 для завершення з "Так"
            return (INT_PTR)TRUE;
        }

        if (LOWORD(wParam) == ID_CANCEL2) // Кнопка "Відміна"
        {
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

int Func_MOD3(HWND hWnd, HINSTANCE hi)
{
    return DialogBox(hi, MAKEINTRESOURCE(IDD_DIALOG3), hWnd, Work3);
}
