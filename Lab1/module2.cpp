#include "module2.h"
#include "resource2.h"

static INT_PTR CALLBACK Work2(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK)
        {
            EndDialog(hDlg, 1);
            return (INT_PTR)TRUE;
        }

        if (LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }

        break;
    }
    return (INT_PTR)FALSE;
}

int Func_MOD2(HWND hWnd, HINSTANCE hi)
{
    return DialogBox(hi, MAKEINTRESOURCE(IDD_DIALOG2), hWnd, Work2);
}