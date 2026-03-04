class ColorPalette {
    constructor() {
        this.colors = this.loadColors();
        this.init();
    }

    init() {
        this.renderColors();
        this.setupEventListeners();
    }

    setupEventListeners() {
        document.getElementById('colorForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleFormSubmit();
        });

        document.getElementById('colorType').addEventListener('change', () => {
            this.clearErrors();
        });
    }

    handleFormSubmit() {
        this.clearErrors();

        const name = document.getElementById('colorName').value.trim();
        const type = document.getElementById('colorType').value;
        const code = document.getElementById('colorCode').value.trim();

        let isValid = true;

        // Проверка названия
        if (!name) {
            this.showError('nameError', 'Название обязательно для заполнения');
            isValid = false;
        } else if (!/^[a-zA-Z]+$/i.test(name)) {
            this.showError('nameError', 'Название должно содержать только буквенные символы');
            isValid = false;
        } else if (this.isNameExists(name)) {
            this.showError('nameError', 'Цвет с таким названием уже существует');
            isValid = false;
        }

        // Проверка кода цвета
        if (!code) {
            this.showError('codeError', 'Код цвета обязателен для заполнения');
            isValid = false;
        } else {
            const codeValid = this.validateColorCode(code, type);
            if (!codeValid) {
                isValid = false;
            }
        }

        if (isValid) {
            this.addColor({ name, type, code });
            this.resetForm();
        }
    }

    validateColorCode(code, type) {
        switch (type) {
            case 'RGB':
                return this.validateRGB(code);
            case 'RGBA':
                return this.validateRGBA(code);
            case 'HEX':
                return this.validateHEX(code);
            default:
                return false;
        }
    }

    validateRGB(code) {
        const regex = /^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$/;
        const match = code.match(regex);
        
        if (!match) {
            this.showError('codeError', 'Неверный формат RGB. Используйте: 0-255, 0-255, 0-255');
            return false;
        }

        for (let i = 1; i <= 3; i++) {
            const value = parseInt(match[i], 10);
            if (value < 0 || value > 255) {
                this.showError('codeError', `Значение ${value} вне диапазона 0-255`);
                return false;
            }
        }
        return true;
    }

    validateRGBA(code) {
        const regex = /^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*([01](?:\.\d+)?)$/;
        const match = code.match(regex);
        
        if (!match) {
            this.showError('codeError', 'Неверный формат RGBA. Используйте: 0-255, 0-255, 0-255, 0.0-1.0');
            return false;
        }

        // Проверяем первые три значения (RGB)
        for (let i = 1; i <= 3; i++) {
            const value = parseInt(match[i], 10);
            if (value < 0 || value > 255) {
                this.showError('codeError', `Значение ${value} вне диапазона 0-255`);
                return false;
            }
        }

        // Проверяем альфа-канал
        const alpha = parseFloat(match[4]);
        if (alpha < 0 || alpha > 1) {
            this.showError('codeError', `Альфа-канал ${alpha} вне диапазона 0-1`);
            return false;
        }
        
        return true;
    }

    validateHEX(code) {
        const regex = /^#[0-9A-Fa-f]{6}$/;
        if (!regex.test(code)) {
            this.showError('codeError', 'Неверный формат HEX. Используйте: #RRGGBB (6 символов)');
            return false;
        }
        return true;
    }

    isNameExists(name) {
        const lowerName = name.toLowerCase();
        return this.colors.some(color => color.name.toLowerCase() === lowerName);
    }

    addColor(color) {
        this.colors.push(color);
        this.saveColors();
        this.renderColors();
    }

    renderColors() {
        const container = document.getElementById('colorsList');
        container.innerHTML = '';

        if (this.colors.length === 0) {
            container.innerHTML = '<p>Цвета не добавлены</p>';
            return;
        }

        this.colors.forEach(color => {
            const colorItem = document.createElement('div');
            colorItem.className = 'color-item';
            
            let backgroundStyle = '';
            if (color.type === 'HEX') {
                backgroundStyle = `background-color: ${color.code};`;
            } else if (color.type === 'RGB') {
                const rgbValues = color.code.split(',').map(val => val.trim());
                backgroundStyle = `background-color: rgb(${rgbValues.join(',')});`;
            } else if (color.type === 'RGBA') {
                const rgbaValues = color.code.split(',').map(val => val.trim());
                backgroundStyle = `background-color: rgba(${rgbaValues.join(',')});`;
            }

            colorItem.innerHTML = `
                <div class="color-preview" style="${backgroundStyle}"></div>
                <div class="color-name">${color.name}</div>
                <div class="color-code">${color.type}: ${color.code}</div>
            `;
            
            container.appendChild(colorItem);
        });
    }

    resetForm() {
        document.getElementById('colorForm').reset();
        this.clearErrors();
    }

    clearErrors() {
        document.getElementById('nameError').textContent = '';
        document.getElementById('codeError').textContent = '';
    }

    showError(elementId, message) {
        document.getElementById(elementId).textContent = message;
    }

    saveColors() {
        // Устанавливаем срок жизни куки — 3 часа
        const date = new Date();
        date.setTime(date.getTime() + (3 * 60 * 60 * 1000)); // 3 часа в миллисекундах
        
        document.cookie = `colors=${JSON.stringify(this.colors)}; expires=${date.toUTCString()}; path=/`;
    }

    loadColors() {
        const name = 'colors=';
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) === 0) {
                try {
                    return JSON.parse(c.substring(name.length, c.length));
                } catch (e) {
                    console.error('Ошибка при загрузке цветов из куки:', e);
                    return [];
                }
            }
        }
        return [];
    }
}

// Инициализация приложения после загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
    new ColorPalette();
});
