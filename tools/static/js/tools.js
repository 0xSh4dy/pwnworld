var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var calculateBtn = document.getElementById("calculate");
var outputSection = document.getElementById("outputValue");
var inputData = document.getElementById("inputData");
var hashBtn = document.querySelectorAll(".hashbtn");
var mode = document.getElementById("mode");
var clearBtn = document.getElementById("clear");
var converterBtn = document.querySelectorAll(".converterBtn");
var formData1 = document.getElementById("formData1");
var formData2 = document.getElementById("formData2");
var result;
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
function calc(dataToModify, method) {
    return __awaiter(this, void 0, void 0, function () {
        var body, response;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    outputSection.innerHTML = "Calculating...";
                    body = {
                        val1: dataToModify,
                        val2: method
                    };
                    response = "";
                    return [4 /*yield*/, axios({
                            method: "POST",
                            url: "http://127.0.0.1:8000/tools/encDec",
                            data: body
                        })];
                case 1:
                    response = _a.sent();
                    result = response.data;
                    outputSection.innerHTML = result;
                    return [2 /*return*/];
            }
        });
    });
}
hashBtn.forEach(function (btn) {
    btn.addEventListener("click", function () {
        mode.innerHTML = btn.innerHTML;
    });
});
converterBtn.forEach(function (btn) {
    btn.addEventListener("click", function () {
        mode.innerHTML = btn.innerHTML;
    });
});
clearBtn.addEventListener("click", function () {
    outputSection.innerHTML = '';
    inputData.value = '';
});
calculateBtn.addEventListener("click", function () {
    var curMode = mode.innerHTML;
    var mainMode;
    var inputVal = inputData.value;
    // if (curMode === "md5" || curMode === "sha1" || curMode === "sha256" || curMode === "sha512") {
    //     mainMode = "hash";
    // }
    if (curMode === "md5") {
        result = md5(inputVal);
    }
    else if (curMode === "sha1") {
        result = sha1(inputVal);
    }
    else if (curMode === "sha256") {
        result = sha256(inputVal);
    }
    else if (curMode === "sha512") {
        result = sha512(inputVal);
    }
    else if (curMode === "base64 encode") {
        result = btoa(inputVal);
    }
    else if (curMode === "base64 decode") {
        try {
            result = atob(inputVal);
        }
        catch (e) {
            result = "Invalid input";
        }
    }
    else if (curMode === "base32 encode") {
        calc(inputVal, "base32encode");
    }
    else if (curMode === "base32 decode") {
        calc(inputVal, "base32decode");
    }
    else if (curMode === "to hex") {
        calc(inputVal, "toHex");
    }
    else if (curMode === "hex decode") {
        calc(inputVal, "fromHex");
    }
    else if (curMode === "decode binary string") {
        calc(inputVal, "decodeBS");
    }
    else if (curMode === "to binary String") {
        calc(inputVal, "toBS");
    }
    outputSection.innerHTML = result;
    // let data = string(inputData.value);
    // switch(modes){
    //     case "md5"
    // }
});
