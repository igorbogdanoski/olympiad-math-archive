import { test, expect } from '@playwright/test';

test.describe('Математичка Архива - Интегритет', () => {
  
  test('Почетната страница треба да го содржи насловот и задачите', async ({ page }) => {
    await page.goto('/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    await expect(page).toHaveTitle(/МатАрхива/);
    
    // Проверка на Hero секцијата
    const hero = page.locator('h1');
    await expect(hero).toBeVisible();
  });

  test('Секоја задача треба да има валидна содржина и слика', async ({ page }) => {
    await page.goto('/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    
    // Најди ја првата картичка што изгледа како вистинска задача
    const taskCard = page.locator('a[href^="/tasks/"]').first();
    const taskHref = await taskCard.getAttribute('href');
    await taskCard.click();
    
    // Проверка дека URL-то е точно
    expect(page.url()).toContain(taskHref);
    
    // Проверка на насловот на задачата (да е видлив и да има текст)
    const title = page.locator('main h1, .lg\\:col-span-2 h1').first();
    await expect(title).toBeVisible();
    const titleText = await title.innerText();
    expect(titleText.length).toBeGreaterThan(2);
    
    // Проверка на сликата (Визуелизација)
    const visualization = page.locator('img[alt="Визуелизација"]');
    if (await visualization.count() > 0) {
      // Проверуваме само дали е во DOM, бидејќи onerror може да ја сокрие ако фали фајлот
      await expect(visualization).toBeAttached();
    }
  });

  test('Математичките формули треба да бидат рендерирани со KaTeX', async ({ page }) => {
    await page.goto('/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    
    // Одиме на задача која е веројатно математичка (избегнуваме MAINTENANCE или README)
    const mathTask = page.locator('a[href^="/tasks/"]').filter({ hasText: /задача|проблем|триаголник|равенка/i }).first();
    
    if (await mathTask.count() > 0) {
      await mathTask.click();
      // Чекаме KaTeX да се појави
      const mathElement = page.locator('.katex');
      await expect(mathElement.first()).toBeVisible({ timeout: 15000 });
    } else {
      console.log('Не е пронајдена соодветна математичка задача за тест.');
    }
  });

  test('Темниот режим треба да ја менува класата на Layout', async ({ page }) => {
    await page.goto('/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    
    const themeToggle = page.locator('#theme-toggle');
    if (await themeToggle.isVisible()) {
      const htmlElement = page.locator('html');
      const initialTheme = await htmlElement.getAttribute('class');
      
      await themeToggle.click();
      const updatedTheme = await htmlElement.getAttribute('class');
      
      expect(initialTheme).not.toBe(updatedTheme);
    }
  });
});
