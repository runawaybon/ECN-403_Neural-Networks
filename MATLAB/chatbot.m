function varargout = chatbot(varargin)
% CHATBOT MATLAB code for chatbot.fig
%      CHATBOT, by itself, creates a new CHATBOT or raises the existing
%      singleton*.
%
%      H = CHATBOT returns the handle to a new CHATBOT or the handle to
%      the existing singleton*.
%
%      CHATBOT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CHATBOT.M with the given input arguments.
%
%      CHATBOT('Property','Value',...) creates a new CHATBOT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before chatbot_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to chatbot_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help chatbot

% Last Modified by GUIDE v2.5 25-Sep-2021 14:02:00

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @chatbot_OpeningFcn, ...
                   'gui_OutputFcn',  @chatbot_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before chatbot is made visible.
function chatbot_OpeningFcn(hObject, ~, handles, varargin)
% This function has no statictext1 args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to chatbot (see VARARGIN)

% Choose default command line statictext1 for chatbot
handles.statictext1 = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes chatbot wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = chatbot_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning statictext1 args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line statictext1 from handles structure
varargout{1} = handles.statictext1;



function input_Callback(hObject, eventdata, handles)
% hObject    handle to input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of input as text
%        str2double(get(hObject,'String')) returns contents of input as a double


% --- Executes during object creation, after setting all properties.
function input_CreateFcn(hObject, eventdata, handles)
% hObject    handle to input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in button.
function button_Callback(hObject, eventdata, handles)
% hObject    handle to button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)







%%%%%%%% OUR CODE %%%%%%%%
system('python D:\Matlab\files\chatbot.py');
    
    
    
    
    
    
    
    
    
