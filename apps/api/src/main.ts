import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import * as OpenApiValidator from 'express-openapi-validator';
import { join } from 'path';
import { OpenApiExceptionFilter } from './openapi-exception.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.setGlobalPrefix('api');

  // Apply OpenAPI Validator Middleware
  app.use(
    OpenApiValidator.middleware({
      apiSpec: join(__dirname, '../../docs/openapi.yaml'),
      validateRequests: true,
      validateResponses: true,
    }),
  );

  // Apply the custom exception filter to format validation errors
  app.useGlobalFilters(new OpenApiExceptionFilter());

  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
