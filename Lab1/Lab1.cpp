// Lab1.cpp : Defines the entry point for the application.
//

#include "framework.h"
#include "Lab1.h"
#include "module1.h"
#include "module2.h"
#include "module3.h"

#define MAX_LOADSTRING 100

// Global Variables:
HINSTANCE hInst;                                // current instance
WCHAR szTitle[MAX_LOADSTRING];                  // The title bar text
WCHAR szWindowClass[MAX_LOADSTRING];            // the main window class name

WCHAR szMyText[4] = L"";

// Forward declarations of functions included in this code module:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);

void onPaint(HWND hWnd);

void DoWork1(HWND hWnd);
void DoWork2(HWND hWnd);

int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPWSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: Place code here.

    // Initialize global strings
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_LAB1, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Perform application initialization:
    if (!InitInstance (hInstance, nCmdShow))
    {
        return FALSE;
    }

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_LAB1));

    MSG msg;

    // Main message loop:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int) msg.wParam;
}



//
//  FUNCTION: MyRegisterClass()
//
//  PURPOSE: Registers the window class.
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
    WNDCLASSEXW wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = hInstance;
    wcex.hIcon          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_LAB1));
    wcex.hCursor        = LoadCursor(nullptr, IDC_ARROW);
    wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.lpszMenuName   = MAKEINTRESOURCEW(IDC_LAB1);
    wcex.lpszClassName  = szWindowClass;
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassExW(&wcex);
}

//
//   FUNCTION: InitInstance(HINSTANCE, int)
//
//   PURPOSE: Saves instance handle and creates main window
//
//   COMMENTS:
//
//        In this function, we save the instance handle in a global variable and
//        create and display the main program window.
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   hInst = hInstance; // Store instance handle in our global variable

   HWND hWnd = CreateWindowW(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, nullptr, nullptr, hInstance, nullptr);

   if (!hWnd)
   {
      return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

//
//  FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  PURPOSE: Processes messages for the main window.
//
//  WM_COMMAND  - process the application menu
//  WM_PAINT    - Paint the main window
//  WM_DESTROY  - post a quit message and return
//
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_COMMAND:
        {
            int wmId = LOWORD(wParam);
            // Parse the menu selections:
            switch (wmId)
            {
            case ID_ACTIONS_WORK1:
                DoWork1(hWnd);
                break;

            case ID_ACTIONS_WORK2:
                DoWork2(hWnd);
                break;

            case IDM_ABOUT:
                DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
                break;

            case IDM_EXIT:
                DestroyWindow(hWnd);
                break;

            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;
    case WM_PAINT:
        onPaint(hWnd);
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// Message handler for about box.
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK_ABOUT || LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}


void onPaint(HWND hWnd) 
{
    PAINTSTRUCT ps;
    HDC hdc = BeginPaint(hWnd, &ps);

    RECT rc;
    GetClientRect(hWnd, &rc);

    HFONT hFontOld;
    HFONT hFontNew;

    int fontSize = 100;  // Розмір шрифту в пікселях
    hFontNew = CreateFont(
        fontSize,                   // Висота шрифту
        0,                         // Ширина шрифту (0 означає автоматичний розрахунок)
        0,                         // Кут обертання шрифту (0 для горизонтального тексту)
        0,                         // Кут обертання тексту (0 для горизонтального тексту)
        FW_NORMAL,                  // Товщина шрифту (FW_BOLD для жирного)
        FALSE,                      // Курсив (TRUE для курсивного шрифту)
        FALSE,                      // Підкреслений (TRUE для підкресленого шрифту)
        FALSE,                      // Перекреслений (TRUE для перекресленого шрифту)
        DEFAULT_CHARSET,            // Набір символів
        OUT_OUTLINE_PRECIS,         // Точність виходу шрифту
        CLIP_DEFAULT_PRECIS,        // Точність обрізання шрифту
        DEFAULT_QUALITY,            // Якість шрифту
        DEFAULT_PITCH | FF_SWISS,   // Ширина і стиль шрифту
        L"Arial");                  // Назва шрифту

    hFontOld = (HFONT)SelectObject(hdc, hFontNew);

    SIZE textSize;
    GetTextExtentPoint32(hdc, szMyText, wcslen(szMyText), &textSize);

    int textWidth = textSize.cx;
    int textHeight = textSize.cy;

    int centerX = (rc.left + rc.right - textWidth) / 2;
    int centerY = (rc.top + rc.bottom - textHeight) / 2;
    
    TextOut(hdc, centerX, centerY, szMyText, 4);

    EndPaint(hWnd, &ps);
}


void DoWork1(HWND hWnd)
{
    Func_MOD1(hWnd, hInst, szMyText) == 1;
    InvalidateRect(hWnd, 0, TRUE);
}


void DoWork2(HWND hWnd)
{
    if (Func_MOD2(hWnd, hInst) == 1) // Якщо натиснуто "Далі >"
    {
        while (true)
        {
            int result = Func_MOD3(hWnd, hInst); // Відкриваємо друге вікно
            if (result == -1) // Якщо натиснуто "< Назад"
            {
                int result2 = Func_MOD2(hWnd, hInst); // Повернення до першого вікна
                if (result2 == 0) // Якщо натиснуто "Відміна" у першому діалозі після повернення
                {
                    break; // Вихід з циклу
                }
            }
            else
            {
                break; // "Відміна" або "Так"
            }
        }
    }
}