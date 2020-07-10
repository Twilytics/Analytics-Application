import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SamplePageOneComponent } from './sample-page-one.component';

describe('SamplePageOneComponent', () => {
  let component: SamplePageOneComponent;
  let fixture: ComponentFixture<SamplePageOneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SamplePageOneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SamplePageOneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
