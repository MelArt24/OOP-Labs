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
        if (LOWORD(wParam) == IDC_BACK) // ������ "< �����"
        {
            EndDialog(hDlg, -1); // ������� 2 ��� �������� �� ������� ���������� ����
            return (INT_PTR)TRUE;
        }

        if (LOWORD(wParam) == IDS_YES) // ������ "���"
        {
            EndDialog(hDlg, 1); // ������� 1 ��� ���������� � "���"
            return (INT_PTR)TRUE;
        }

        if (LOWORD(wParam) == ID_CANCEL2) // ������ "³����"
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
